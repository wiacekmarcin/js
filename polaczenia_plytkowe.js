app.controller('polaczenia_plytkowe-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.plytki= [];
    $scope.plytka_id = 0;

    $scope.editRow = {'id' : -1};
    $scope.addRow = {'id' : 1, "add" : false};
    $scope.showRowId = -1;
    

    var get = function() {

        $http.get("polaczenia_plytkowe_list.php").then(function(response) { 
            $scope.plytki = response.data.plytki;
            $scope.plytkilist = response.data.plytkilist;
            $scope.polaczenia = response.data.polaczenia;
            $scope.ilosc_pin = response.data.ilosc_pin;

        });
    };


    get();
}]);