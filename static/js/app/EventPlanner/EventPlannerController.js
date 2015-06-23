EventPlannerModule.config(function ($routeProvider) {
    // TODO: Fix the routes' names
    $routeProvider.when('/VHome', {
                controller: 'VHomeController',
                templateUrl: 'app/EventPlanner/VHome.html'
            })
});

EventPlannerModule.controller('VHomeController', 
        ['$scope', '$location', '$route', 'flash', 'EventPlannerService',
    function ($scope, $location, $route, flash, EventPlannerService) {
      $scope.msg = '';
      EventPlannerService.VHome().then(function (object) {
        console.log($scope); 
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
        if (object.data['actor']) {
            $scope.user = object.data['actor']; 
        }  
      });

      $scope.AEvents = function() {
        EventPlannerService.AEvents().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VHome') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};
      $scope.AEvents1 = function(requestedEvent) {
        EventPlannerService.AEvents({"requestedEvent":((typeof requestedEvent === 'object')?JSON.stringify(requestedEvent):requestedEvent)}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VHome') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};

        $scope.AUsers2 = function() {
        EventPlannerService.AUsers().then(function (object) {
          var msg = object.data["msg"];
          var users = object.data["users"];
          if (users) flash(users)
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VHome') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};
        $scope.NewEvent = function() {
            $location.path('/events/new');
          };

    }]);
