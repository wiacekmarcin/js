app.controller('zakonczenieedit-ctrl', ['$scope', '$routeParams', '$location', '$http', 
function($scope, $routeParams, $location, $http) {
    var zid = $routeParams.id;
    $http.get("zakonczenie_edit.php?zid=" + zid).then(function(response) { 
        $scope.zakonczenie = response.data.zakonczenie;
        $scope.zyly = response.data.zyly;
        $scope.kolory = response.data.kolory;
    });
}]);