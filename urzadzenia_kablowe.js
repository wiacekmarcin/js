app.controller('urzadzenia_kablowe-ctrl', ['$scope', '$http', function($scope, $http) {

    $scope.editRow = { id : -1};
    $scope.addRow = { id : 0 };

    $http.get("urzadzenia_kablowe_list.php").then(function(response) { 
        $scope.urzadzenia = response.data.urzadzenia;
        $scope.rodzaj = response.data.rodzaj;
        $scope.przewodmiejsce = response.data.przewodmiejsce;
        $scope.allpins = response.data.pins;
    });

    
    
    $scope.setEdit = function(urz) {
        $scope.editRow = {
            "id" : urz.id,
            "nazwa" : urz.nazwa,
            "ilosc_pin" : urz.ilosc_pin,
            "rodzaj_id" : $scope.rodzaj[urz.rodzaj_zakonczenia],
            "przewod_miejsce_id" : urz.przewod_miejsce_id,
            "zakonczenie_id" : urz.id
        }
    }
    
    $scope.cancelEdit = function() {
        $scope.editRow = {
            "id" : -1,
        }
    }

    $scope.saveEdit = function() {
        $scope.editRow.rodzaj = $scope.editRow.rodzaj_id.$key;
        sendData($scope.editRow);
    }

    $scope.saveAdd = function() {
        sendData({
            "edit" : "false",
            "id" : $scope.addRow.id,
            "nazwa" : $scope.addRow.nazwa,
            "ilosc_pinow" : $scope.addRow.ilosc_pin,
            "rodzaj" : $scope.addRow.rodzaj_id.$key,
            "przewod_miejsce_id" : -1*$scope.addRow.zakonczenie_id,
            "zakonczenie_id" : -1,
        });
    };

    $scope.cancelAdd = function() {
        $scope.addRow = { "id" : 0 };
    };

    $scope.addAdd = function() {
        $scope.addRow = { "id" : -1 };
    }

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
            url: "urzadzenia_kablowe_ins.php",
            data: toparams(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then( function success(response) {
            $scope.cancelAdd();
            get();
        }, function error(response) {
            alert("Nie Udało się") ;
        });
    };

    $scope.setDetails = function (uid) {
        $scope.showRowId = uid;
        $scope.chDetails = 0;
        $scope.pins = $scope.allpins[uid];
    };

}]);