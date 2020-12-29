app.controller('polaczenia_plytkowe-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.plytki= [];
    $scope.plyta_id = { '$key' : 0 };

    $scope.editRow = {'id' : -1};
    $scope.addRow = {'id' : 1, "add" : false};
    $scope.showRowId = -1;
    $scope.addaddPolaczenie = false;

    var get = function() {

        $http.get("polaczenia_plytkowe_list.php").then(function(response) { 
            $scope.plytki = response.data.plytki;
            $scope.plytkilist = response.data.plytkilist;
            $scope.polaczenia = response.data.polaczenia;
            $scope.ilosc_pin = response.data.ilosc_pin;
            $scope.polaczenienazwane = response.data.polaczenienazwane;
        });
    };

    $scope.selectPlytka = function(showAll) {
        if (showAll) {
            $scope.plyta_id =  $scope.plytka_id ;
            $scope.plytka_id = undefined;
        } else {
            $scope.plyta_id = { '$key' : 0 };
            $scope.plytka_id = undefined;
        }
    }

    $scope.addPolaczenie = function(add) {
        $scope.addaddPolaczenie = add;
    }

    $scope.addPin = function(save) {
        if (save) {
            //save
        } else {
            $scope.addPolaczenie(false);
        }
    }

    get();
}]);