app.controller('kolory-ctrl', function($scope, $http) {
    $http.get("kolory_list.php")
        .then(function(response) {
            $scope.colors = response.data.records;
        });
    $scope.editColorId = -1;
  });