app.controller('zylaeadd-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.id_miejsce = -1;
    $scope.przewody = []
    $scope.zyla2 = {};
    $http.get("zyla_add.php").then(function(response) { 
        //$scope.zbiorcze = response.data.zbiorcze;
        //$scope.przewody = response.data.przewody;
        //$scope.zlacza = response.data.zlacza;
        //$scope.zyly = response.data.zyly;
        //$scope.miejsca = response.data.miejsca;
    });
}]);