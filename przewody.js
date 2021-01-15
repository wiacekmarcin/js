app.controller('przewody-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.selectZbiorcze = -1;

    $scope.detailsAll = false;

    $scope.editzyla = -1;
    $scope.editRow = {'id' : -1};
    $scope.addRow = {'id' : 1, "add" : false};
    $scope.editkolor = false;
    $scope.editopis = false;


    $scope.zylaedit =  {}
    var get = function() {

        $http.get("przewody_list.php").then(function(response) { 

            $scope.przewody = response.data.przewody;
            $scope.prze = response.data.przewod;
            $scope.zyla = response.data.zyla;
            $scope.miej = response.data.miejsce;
            $scope.przew_miej = response.data.przewod_miejsce;
            $scope.zakonczenie = response.data.zakonczenie;
            $scope.polaczenia = response.data.polaczenia;
            $scope.urzadzenia = response.data.urzadzenia;
            $scope.kolory = response.data.kolory;

            var BreakException = {};
            for (var i=0; i < $scope.przewody.length; i++) {
                if ($scope.przewody[i] == $scope.addRow.id) {
                    $scope.addRow.id +=  1;
                } else {
                    i = $scope.przewody.length;
                }
            }
        });
    };

    get();

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
    
    $scope.isShowWire = function(wire_id) {
        return $scope.selectZbiorcze == -1 ||
                $scope.prze[wire_id]["miejsca"][0]["mid"] == $scope.selectZbiorcze ||
                $scope.prze[wire_id]["miejsca"][1]["mid"] == $scope.selectZbiorcze;
    }


    $scope.showtd1 = function(wire_id) {
        return $scope.prze[wire_id]["miejsca"][0]["mid"] == $scope.selectZbiorcze;
    }

    $scope.showtd2 = function(wire_id) {
        return $scope.prze[wire_id]["miejsca"][1]["mid"] == $scope.selectZbiorcze;
    }
    
    $scope.showtd3 = function(wire_id) {
        return $scope.prze[wire_id]["miejsca"][0]["mid"] != $scope.selectZbiorcze;
    }
    $scope.showtd4 = function(wire_id) {
        return $scope.prze[wire_id]["miejsca"][1]["mid"] != $scope.selectZbiorcze;
    }

    $scope.seteditPlace = function(pid) {
        $scope.editRow = {
            "id" : pid,
            "opis" : $scope.prze[pid].opis,
            "ilosc_zyl" : $scope.prze[pid].ilosc_zyl,
            "miejsce_id1" : $scope.miej[$scope.prze[pid]["miejsca"][0].mid],
            "miejsce_id2" : $scope.miej[$scope.prze[pid]["miejsca"][1].mid],
            "pmid_1" : $scope.prze[pid]["miejsca"][0].pmid,
            "pmid_2" : $scope.prze[pid]["miejsca"][1].pmid,
        }
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
            "miejsce_id_1" : $scope.editRow.miejsce_id1.$key,
            "miejsce_id_2" : $scope.editRow.miejsce_id2.$key,
            "pmid_1" : $scope.editRow.pmid_1,
            "pmid_2" : $scope.editRow.pmid_2
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
            "opis" : $scope.addRow.opis,
            "ilosc_zyl" : $scope.addRow.ilosc_zyl,
            "miejsce_id_1" : $scope.addRow.miejsce_id1.$key,
            "miejsce_id_2" : $scope.addRow.miejsce_id2.$key,
            "pmid_1" : -1,
            "pmid_2" : -1,
        });
        
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
    };

    $scope.setEditZyla = function (przewod_id)
    {
        $scope.editzyla = przewod_id;
        if ($scope.prze[przewod_id]) {
            for (var z in $scope.prze[przewod_id]["zyly"]) {
                $scope.zylaedit[$scope.prze[przewod_id]["zyly"][z]] = $scope.zyla[$scope.prze[przewod_id]["zyly"][z]];
            }
        } else{
            
        }
    };

    $scope.saveEditZyla = function(przewod_id) {
        params = {};
        var i = 0;
        if ($scope.prze[przewod_id]) {
            for (var z in $scope.prze[przewod_id]["zyly"]) {
                params["id_" + i] = $scope.prze[przewod_id]["zyly"][z];
                params["kolor_" + i] =  $scope.zylaedit[$scope.prze[przewod_id]["zyly"][z]].kolor_id;
                params["opis_" + i] =  $scope.zylaedit[$scope.prze[przewod_id]["zyly"][z]].opis;
                i += 1;
            }
        }
        params["przewod"] = przewod_id;
        params["count"] = i;
    }

}]);

