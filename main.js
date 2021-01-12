app.controller('main-ctrl', function($scope, $http) {
  $http.get("stat.php")
        .then(function(response) {

          $scope.przewod = response.data.przewod;
          $scope.zyla = response.data.zyla;
          $scope.zyla_all = response.data.zyla_all;
          $scope.zlacze = response.data.zlacze;
          $scope.zewn_przew = response.data.zewn_przew;
          $scope.wewn_przew = response.data.wewn_przew;
          $scope.zakonczenia = response.data.zakonczenia;
          $scope.kolory = response.data.kolory;
          $scope.przewod_opis = response.data.przewod_opis;
        });
});