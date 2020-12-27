app.controller('elementy_plytkowe-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.elementy= [];

    $scope.editRow = {'id' : -1};
    $scope.addRow = {'id' : 1, "add" : false};
    $scope.showRowId = -1;
    

    var get = function() {

        $http.get("elementy_plytkowe_list.php").then(function(response) { 
            $scope.elementy = response.data.elementy;
            $scope.miej = response.data.miejsce;
            $scope.plytki = response.data.plytki;
            $scope.rodzaj = response.data.rodzaj;
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
        $scope.editRow.rodzaj_id = $scope.rodzaj[urz.element_rodzaj_id];
    };

    $scope.setChDetails = function(ch) {
        $scope.chDetails = ch;
    };

    $scope.setDetails = function(did) {
        $scope.showRowId = did;
        $scope.pins = [];
        $scope.chDetails = 0;
        $scope.edit_pins = {};
        
        $http.get("elementy_plytkowe_pin_list.php?id="+did).then(function(response) { 
            $scope.pins = response.data.pins;
            for (var i = 0; i < $scope.pins.length; i++) {
                $scope.edit_pins[$scope.pins[i].id] = {
                    "nazwa" : $scope.pins[i].nazwa,
                    "pos" : $scope.pins[i].pos
                };
            }
        });
    };

    $scope.saveEdit = function() {
        sendData({
            "edit" : "true",
            "id" : $scope.editRow.id,
            "nazwa" : $scope.editRow.nazwa,
            "ilosc_pinow" : $scope.editRow.ilosc_pin,
            "remove_pin" : $scope.ilosc_pinow == $scope.editRow.ilosc_pinow,
            "rodzaj_id" : $scope.editRow.rodzaj_id.$key,
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
            "ilosc_pinow" : $scope.addRow.ilosc_pin,
            "rodzaj_id" : $scope.addRow.rodzaj_id.$key,
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
    };


    $scope.savePins = function(did) {
        var params = {};

        var i = 0;
        for (var p in $scope.edit_pins)
        {
            params["index_" + i] = p;
            i++;
            params["nazwa_" + p] = $scope.edit_pins[p].nazwa;
            params["pos_" + p] = $scope.edit_pins[p].pos;
        }
        params["length"] = i;

        $http({
            method: 'POST',
            url: "elementy_plytkowe_pin_ins.php",
            data: toparams(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then( function success(response) {
            $scope.setDetails(did);
        }, function error(response) {
            alert("Nie Udało się") ;
        });
    }

    get();

}]);