var GoogleAuth;

function initializeClient(scope, apiKey, clientId, discoveryDocs, authControlsId, onSigninStatusChange) {
    // Load the API's client and auth2 modules.
    // Call the initClient function after the modules load.
    gapi.load('client:auth2', function () {
        initClient(scope, apiKey, clientId, discoveryDocs, authControlsId, onSigninStatusChange);
    });
}

function initClient(scope, apiKey, clientId, discoveryDocs, authControlsId, onSigninStatusChange) {
    $(`#${authControlsId}`).html(
        '<button id="sign-in-or-out-button" style="margin-left: 25px">Sign In/Authorize</button>' +
        '<button id="revoke-access-button" style="display: none; margin-left: 25px">Revoke access</button>' +
        '<div id="auth-status" style="display: inline; padding-left: 25px"></div>'
    )

    // Initialize the gapi.client object, which app uses to make API requests.
    // Get API key and client ID from API Console.
    // 'scope' field specifies space-delimited list of access scopes.
    gapi.client.init({
        'apiKey': apiKey,
        'clientId': clientId,
        'discoveryDocs': discoveryDocs,
        'scope': scope
    }).then(function () {
        GoogleAuth = gapi.auth2.getAuthInstance();

        // Listen for sign-in state changes.
        GoogleAuth.isSignedIn.listen(function () { setSigninStatus(scope, onSigninStatusChange); });

        // Handle initial sign-in state. (Determine if user is already signed in.)
        var user = GoogleAuth.currentUser.get();
        setSigninStatus(scope, onSigninStatusChange);

        // Call handleAuthClick function when user clicks on
        //      "Sign In/Authorize" button.
        $('#sign-in-or-out-button').click(function() {
            handleAuthClick();
        });
        $('#revoke-access-button').click(function() {
            revokeAccess();
        });
    });
}

function handleAuthClick() {
    if (GoogleAuth.isSignedIn.get()) {
        // User is authorized and has clicked "Sign out" button.
        GoogleAuth.signOut();
    } else {
        // User is not signed in. Start Google auth flow.
        GoogleAuth.signIn();
    }
}

function revokeAccess() {
    GoogleAuth.disconnect();
}

function setSigninStatus(scope, onSigninStatusChange) {
    var user = GoogleAuth.currentUser.get();
    var isAuthorized = user.hasGrantedScopes(scope);
    if (isAuthorized) {
        $('#sign-in-or-out-button').html('Sign out');
        $('#revoke-access-button').css('display', 'inline-block');
        $('#auth-status').html(`You are currently signed in as ${user.getBasicProfile().getEmail()} and have granted access to this app.`);
        onSigninStatusChange(user);
    } else {
        $('#sign-in-or-out-button').html('Sign In/Authorize');
        $('#revoke-access-button').css('display', 'none');
        $('#auth-status').html('You have not authorized this app or you are signed out.');
        onSigninStatusChange(null);
    }
}
