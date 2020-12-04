app.controller('przewody-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.selectZbiorcze = -1;
    $scope.wires = [];
    $scope.detailsAll = false;

    $scope.editRow = {'id' : -1};
    $scope.addRow = {'id' : 1, "add" : false};
    

    var get = function() {

        $http.get("przewody_list.php").then(function(response) { 
            $scope.miejsca_przewody = response.data.miejsca_przewody;
            $scope.przewody = response.data.przewody;
            $scope.zyly = response.data.zyly;
            $scope.miejsca = response.data.miejsca;
            var BreakException = {};
            for (var i=0; i < $scope.przewody.length; i++) {
                if ($scope.przewody[i].id == $scope.addRow.id) {
                    $scope.addRow.id +=  1;
                } else {
                    i = $scope.przewody.length;
                }
            }
            /*
            try {
                $scope.przewody.forEach(function(value, key, przewody) {
                    if (value.id == $scope.addRow.id) {
                        
                    } else {
                        throw BreakException;
                    }
                });
            } catch (e) {
                if (e !== BreakException) throw e;
            }
            */

            //$scope.choose(-1);
        });
    };

    get();

    $scope.myFilter = function (item) { 
        return item.zbiorcze == 1 || item.polaczenie == 1; 
    };

    $scope.choose = function(id, name) {
        $scope.selectZbiorcze = id;
        $scope.chooseName = name;
    };

    $scope.setDetails = function(id) {
        $scope.detailsId = id;
    };

    $scope.setDetailsAll = function() {
        $scope.detailsAll = !$scope.detailsAll;
    };
    
    $scope.seteditPlace = function(row) {
        $scope.editRow = row;
        if ($scope.selectZbiorcze != -1) {
            $scope.editRow.miejsce_id1 = $scope.selectZbiorcze;
        } else {
            $scope.editRow.miejsce_id1 = $scope.miejsca[$scope.miejsca_przewody[row.id][0].miejsce_id];
        }
        $scope.editRow.miejsce_id2 = $scope.miejsca[$scope.miejsca_przewody[row.id][1].miejsce_id];
    };

    $scope.cancelEdit = function() {
        $scope.editRow = {'id' : -1};
    };

    $scope.saveEdit = function() {
        sendData({
            "edit" : "true",
            "id" : $scope.editRow.id,
            "opis" : $scope.editRow.opis,
            "ilosc_zyl" : $scope.editRow.ilosc_zyl,
            "miejsce_id_1" : $scope.editRow.miejsce_id1.id,
            "miejsce_id_2" : $scope.editRow.miejsce_id2.id
        })
    };

    $scope.addAdd = function() {
        $scope.addRow.add = true;
    };    

    $scope.saveAdd = function() {
        sendData({
            "edit" : "false",
            "id" : $scope.addRow.id,
            "opis" : $scope.addRow.opis,
            "ilosc_zyl" : $scope.addRow.ilosc_zyl,
            "miejsce_id_1" : $scope.addRow.miejsce_id1.id,
            "miejsce_id_2" : $scope.addRow.miejsce_id2.id
        })
    };

    $scope.cancelAdd = function() {
        $scope.addRow.add = false;
        $scope.addRow.opis = '';
        $scope.miejsce_id1 = null;
        $scope.miejsce_id2 = null;
        $scope.ilosc_zyl = 1;
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
            url: "przewody_ins.php",
            data: toparams(params),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then( function success(response) {
            $scope.cancelAdd();
            get();
        }, function error(response) {
            alert("Nie Udało się") ;
        });
    }

}]);

