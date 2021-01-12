app.controller('polaczeniezyla-ctrl', ['$scope', '$http', function($scope, $http) {

    $http.get("polaczenie_zyla.php").then(function(response) { 
        $scope.przewody = response.data.przewody;
        $scope.zyly = response.data.zyly;
    });
}]);