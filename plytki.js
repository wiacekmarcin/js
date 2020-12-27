app.controller('plytki-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.plytki= [];

    $scope.editRow = {'id' : -1};
    $scope.addRow = {'id' : 1, "add" : false};
    $scope.showRowId = -1;
    

    var get = function() {

        $http.get("plytki_list.php").then(function(response) { 
            $scope.plytki = response.data.plytki;
            $scope.urzadzenia = response.data.urzadzenia;
            $scope.miej = response.data.miejsce;
        });
    };

    $scope.cancelEdit = function() {
        $scope.editRow = {'id' : -1};
    };

    $scope.setEdit = function(pl) {
        $scope.editRow = pl;
        $scope.editRow.miejsce_id = $scope.miej[pl.miejsce_id];
    };

    $scope.saveEdit = function() {
        sendData({
            "edit" : "true",
            "id" : $scope.editRow.id,
            "nazwa" : $scope.editRow.nazwa,
            "miejsce_id" : $scope.editRow.miejsce_id.$key,
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
            "miejsce_id" : $scope.addRow.miejsce_id.$key,
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
            url: "plytki_ins.php",
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