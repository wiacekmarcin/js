app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "main.htm"
    })
    .when("/kolory", {
        templateUrl : "kolory.htm"
    })
    .when("/miejsca/:id", {
        templateUrl: 'miejsca.htm',    
    })
    .when("/przewody", {
        templateUrl : "przewody.htm"
    })
    .when("/miejsce_view/:id", {
        templateUrl: 'miejsce_view.htm',    
    })
    .when("/zlacza", {
        templateUrl: 'zlacza.htm',    
    })
    .when("/zlacze_add", {
        templateUrl: 'zlacze_add.htm',    
    })
    .when("/polaczenie_add", {
        templateUrl: 'polaczenie_add.htm',    
    })
    .when("/zyla_add", {
        templateUrl: 'zyla_add.htm',    
    })
});