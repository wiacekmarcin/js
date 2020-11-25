app.controller('zlaczeadd-ctrl', ['$scope', '$http', function($scope, $http) {
    $scope.id_miejsce = -1;
    $scope.przewody = []
    $scope.zyla2 = {};
    $http.get("zlacze_add.php").then(function(response) { 
        //$scope.zbiorcze = response.data.zbiorcze;
        //$scope.przewody = response.data.przewody;
        //$scope.zlacza = response.data.zlacza;
        //$scope.zyly = response.data.zyly;
        //$scope.miejsca = response.data.miejsca;
    });

    $scope.zmianaMiejsca = function() {
        $scope.przewody = $scope.id_miejsce.kable;
    }

    $scope.zmianaPrzewodu1 = function() {
        $scope.zyly1 = $scope.zyly[$scope.przewod1];
    }

    $scope.zmianaPrzewodu2 = function() {
        $scope.zyly2 = $scope.zyly[$scope.przewod2];
    }

    $scope.zmianaZyly2 = function(id) {
        $scope.z1 = id;
        $scope.z2 = $scope.zyla2[id].id;
    }
}]);