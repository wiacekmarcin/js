app.controller('przewody-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.selectZbiorcze = -1;
    $scope.wires = [];
    $scope.detailsAll = false;
    $scope.editRow = -1;
    $scope.edescr = '';
    $http.get("przewody_list.php").then(function(response) { 
        $scope.zbiorcze = response.data.zbiorcze;
        $scope.allwires = response.data.przewody;
        $scope.zyly = response.data.zyly;
        //$scope.miejsca = response.data.miejsca;
        $scope.choose(-1);
    });

    $scope.choose = function(id, name) {
        $scope.selectZbiorcze = id;
        $scope.chooseName = name;
        $scope.wires = [];
        $scope.detailsId = -1;
        $scope.detailsAll = false;
        for (var i = 0; i < $scope.allwires.length; i++){
            row = $scope.allwires[i];
            if (id == -1) {
                if (row['zbiorcze1'] == 1 || (row['zbiorcze1'] == 0 && row['zbiorcze2'] == 0)) {
                    $scope.wires.push({ 'zbiorcze1' : row['zbiorcze1'], 'mid1' : row['mid1'], 'miejsce1' : row['miejsce1'],
                                        'zbiorcze2' : row['zbiorcze2'], 'mid2' : row['mid2'], 'miejsce2' : row['miejsce2'],
                                        'id' : row['id'], 'descr' : row['descr'], 'ilosc_zyl' : row['ilosc_zyl']});
                } else {
                    $scope.wires.push({ 'zbiorcze1' : row['zbiorcze2'], 'mid1' : row['mid2'], 'miejsce1' : row['miejsce2'],
                                        'zbiorcze2' : row['zbiorcze1'], 'mid2' : row['mid1'], 'miejsce2' : row['miejsce1'],
                                        'id' : row['id'], 'descr' : row['descr'], 'ilosc_zyl' : row['ilosc_zyl']});
                }
            } else {
                if (id == row['mid1']) {
                    $scope.wires.push({ 'zbiorcze1' : row['zbiorcze1'], 'mid1' : row['mid1'], 'miejsce1' : row['miejsce1'],
                                        'zbiorcze2' : row['zbiorcze2'], 'mid2' : row['mid2'], 'miejsce2' : row['miejsce2'],
                                        'id' : row['id'], 'descr' : row['descr'], 'ilosc_zyl' : row['ilosc_zyl']});
                } else if (id == row['mid2']) {
                    $scope.wires.push({ 'zbiorcze1' : row['zbiorcze2'], 'mid1' : row['mid2'], 'miejsce1' : row['miejsce2'],
                                        'zbiorcze2' : row['zbiorcze1'], 'mid2' : row['mid1'], 'miejsce2' : row['miejsce1'],
                                        'id' : row['id'], 'descr' : row['descr'], 'ilosc_zyl' : row['ilosc_zyl']});
                }
            }
        }
    }

    $scope.setDetails = function(id) {
        $scope.detailsId = id;
    }

    $scope.setDetailsAll = function() {
        $scope.detailsAll = !$scope.detailsAll;
    }
    
    $scope.seteditPlace = function(id) {
        $scope.editRow = id;
    }
}]);

