app.controller('zlacza-ctrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
    
    $http.get("zlacza.php").then(function(response) { 
        $scope.k_zlacza = response.data.k_zlacza;
        $scope.k_urzadzenia = response.data.k_urzadzenia;
        $scope.k_wtyczki = response.data.k_wtyczki;
        $scope.k_polaczenia_kablowe = response.data.k_polaczenia_kablowe;
        $scope.k_polaczenia_plytkowe = response.data.k_polaczenia_plytkowe;
        $scope.k_inne = response.data.k_inne;
        $scope.p_zlacza = response.data.p_zlacza;
        $scope.p_urzadzenia = response.data.p_urzadzenia;
        $scope.p_wtyczki = response.data.p_wtyczki;
        $scope.p_polaczenia_kablowe = response.data.p_polaczenia_kablowe;
        $scope.p_polaczenia_plytkowe = response.data.p_polaczenia_plytkowe;
        $scope.p_inne = response.data.p_inne;
        $scope.zlacze_wtyczka = response.data.zlacze_wtyczka;
        $scope.wtyczka_zlacze = response.data.wtyczka_zlacze;
        $scope.wtyczki = response.data.wtyczki;
        $scope.zyly = response.data.zyly;
        $scope.piny = response.data.piny;
        $scope.zakon = response.data.zakon;
        $scope.zakonId = response.data.zakonId;
        $scope.plytkaId = response.data.plytkaId;
        $scope.pnazwa = response.data.pnazwa;
        $scope.polaczenia_plytkowe = response.data.polaczenia_plytkowe;
    });

}]);