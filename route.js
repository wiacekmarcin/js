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
    .when("/urzadzenia_kablowe", {
        templateUrl: 'urzadzenia_kablowe.htm',    
    })
    .when("/zlacze_add", {
        templateUrl: 'zlacze_add.htm',    
    })
    .when("/polaczenie_add", {
        templateUrl: 'polaczenie_add.htm',    
    })
    .when("/polaczenie_zyla", {
        templateUrl: 'polaczenie_zyla.htm',    
    })
    .when("/zyla_add/:id", {
        templateUrl: 'zyla_add.htm',    
    })
    .when("/zakonczenie_add/:id", {
        templateUrl: 'zakonczenie_add.htm',    
    })
    .when("/zakonczenie_piny_add/:id", {
        templateUrl: 'zakonczenie_piny_add.htm',    
    })
    .when("/zakonczenie_edit/:id", {
        templateUrl: 'zakonczenie_edit.htm',    
    })
    .when("/elementy_plytkowe", {
        templateUrl: 'elementy_plytkowe.htm',    
    })
    .when("/polaczenia_plytkowe", {
        templateUrl: 'polaczenia_plytkowe.htm',    
    })
    .when("/plytki", {
        templateUrl: 'plytki.htm',    
    })
});