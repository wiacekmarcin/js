app.controller('polaczenieadd-ctrl', ['$scope', '$http', function($scope, $http) {
    $http.get("polaczenie_add.php").then(function(response) { 
        $scope.zbiorcze = response.data.zbiorcze;
        $scope.przewody = response.data.przewody;
        $scope.zlacza = response.data.zlacza;
        $scope.zyly = response.data.zyly;
        $scope.miejsca = response.data.miejsca;
    });
}]);