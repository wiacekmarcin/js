app.controller('elementy_plytkowe-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.urzadzenia= [];

    $scope.editRow = {'id' : -1};
    $scope.addRow = {'id' : 1, "add" : false};
    $scope.showRowId = -1;
    

    var get = function() {

        $http.get("elementy_plytkowe_list.php").then(function(response) { 
            $scope.urzadzenia = response.data.urzadzenia;
            $scope.miej = response.data.miejsce;
            $scope.plytki = response.data.plytki;
        });
    };



    $scope.addAdd = function() {
        $scope.addRow.add = true;
    };

    $scope.cancelAdd = function() {
        $scope.addRow.add = false;
    };

    $scope.cancelEdit = function() {
        $scope.editRow = {'id' : -1};
    };

    $scope.setEdit = function(urz) {
        $scope.editRow = urz;
        $scope.editRow.plytka_id = $scope.plytki[urz.plytka_id];
        $scope.ilosc_pinow = $scope.editRow.ilosc_pinow;
    };

    $scope.setDetails = function(did) {
        $scope.showRowId = did;
        $http.get("elementy_plytkowe_pin_list.php").then(function(response) { 
            $scope.urzadzenia = response.data.urzadzenia;
            $scope.miej = response.data.miejsce;
            $scope.plytki = response.data.plytki;
        });
    }

    $scope.saveEdit = function() {
        sendData({
            "edit" : "true",
            "id" : $scope.editRow.id,
            "nazwa" : $scope.editRow.nazwa,
            "ilosc_pinow" : $scope.editRow.ilosc_pinow,
            "remove_pin" : $scope.ilosc_pinow == $scope.editRow.ilosc_pinow,
            "płytka_id" : $scope.editRow.plytka_id.$key,
        })
        $scope.editRow = {'id' : -1};
    };

    $scope.addAdd = function() {
        $scope.addRow.add = true;
    };    

    $scope.saveAdd = function() {
        sendData({
            "edit" : "false",
            "id" : $scope.addRow.id,
            "nazwa" : $scope.addRow.nazwa,
            "ilosc_pinow" : $scope.editRow.ilosc_pinow,
            "remove_pin" : false,
            "plyta_id" : $scope.addRow.plytka_id.$key,
        });
        
    };

    $scope.cancelAdd = function() {
        $scope.addRow.add = false;
        $scope.addRow.nazwa = '';
        $scope.miejsce_id = null;
    };


    var toparams = function (obj) {
        var p = [];
        for (var key in obj) {
            p.push(key + '=' + encodeURIComponent(obj[key]));
        }
        return p.join('&');
    };
    

    var sendData = function(params) {
        $http({
            method: 'POST',
            url: "elementy_plytkowe_ins.php",
            data: toparams(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then( function success(response) {
            $scope.cancelAdd();
            get();
        }, function error(response) {
            alert("Nie Udało się") ;
        });
    }

    get();

}]);