app.controller('miejsceview-ctrl', ['$scope','$routeParams', '$http', function($scope, $routeParams, $http) {
    var mid = $routeParams.id;
    $http.get("miejsce_view.php?mid="+ mid).then(function(response) { 
        $scope.miejsce  = response.data.miejsce;
        $scope.zewnetrzne = response.data.zewnetrzne;
        $scope.wewnetrzne =  response.data.wewnetrzne;
        $scope.przewody = response.data.przewody;
        $scope.zyly = response.data.zyly;
        $scope.zakonczenia = response.data.zakonczenia;
    });
}]);