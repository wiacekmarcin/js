app.controller('polaczenia_plytkowe-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.plytki= [];
    $scope.plyta_id = { '$key' : 0 };

    $scope.editRow = {'id' : -1};
    $scope.addRow = {'id' : 1, "add" : false};
    $scope.polRow = {id : -1};
    $scope.showRowId = -1;
    $scope.addPol = false;
    $scope.new_pin_element_id = '';

    var get = function() {

        $http.get("polaczenia_plytkowe_list.php").then(function(response) { 
            $scope.plytki = response.data.plytki;
            $scope.plytkilist = response.data.plytkilist;
            $scope.polaczenia = response.data.polaczenia;
            $scope.ilosc_pin = response.data.ilosc_pin;
            $scope.polaczenienazwane = response.data.polaczenienazwane;
            $scope.pins = response.data.pins;
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
    };

    $scope.addPolaczenie = function(pol_id) {
        $scope.polRow.id = pol_id;
    };

    $scope.addNazwanyPin = function(add) {
        $scope.addPol = add;
    }

    $scope.addPin = function(save) {
        if (save) {
            var p = {
                'id' : -1,
                'nazwa' : $scope.nowa_nazwa_polaczenia,
                'plytka_id' : $scope.plyta_id.$key
            };
            sendData("polaczenia_plytkowe_edit.php", p);
        } 
        $scope.addNazwanyPin(false);
        $scope.nowa_nazwa_polaczenia = '';
    };

    $scope.editPin = function(nazwany_pin) {
        $scope.editRow.id = nazwany_pin.id;
        $scope.editRow.nazwa = nazwany_pin.nazwa;
    };

    $scope.savePin = function() {
        var p = $scope.editRow;
        p['plytka_id'] = $scope.plyta_id.$key;

        sendData("polaczenia_plytkowe_edit.php", p);
    };

    $scope.savePolaczenie = function() {
        var id2 = $scope.polRow;
        var p = {
            id : $scope.polRow.id,
            pin : $scope.polRow.pinid.id
        }
        sendData("polaczenia_plytkowe_add.php", p);
    };

    var toparams = function (obj) {
        var p = [];
        for (var key in obj) {
            p.push(key + '=' + encodeURIComponent(obj[key]));
        }
        return p.join('&');
    };
    

    var sendData = function(urlwww, params) {
        $http({
            method: 'POST',
            url: urlwww,
            data: toparams(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then( function success(response) {
            get();
        }, function error(response) {
            alert("Nie Udało się") ;
            get();
        });
    };


    get();
}]);