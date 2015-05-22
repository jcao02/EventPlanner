EventPlannerModule.config(function ($routeProvider) {
    $routeProvider.when('/events', {
                controller: 'ListEventsController',
                templateUrl: 'app/EventPlanner/event/list.html'
            }).when('/event/:id', {
                controller: 'VShowEventController',
                templateUrl: 'app/EventPlanner/VShowEvent.html'
            }).when('/events/edit/:id', {
                controller: 'VEditEventController',
                templateUrl: 'app/EventPlanner/VEditEvent.html'
            }).when('/events/new', {
                controller: 'RegisterEventController',
                templateUrl: 'app/EventPlanner/event/new.html'
 
            })
}); 

EventPlannerModule.controller('RegisterEventController', 
                              ['$scope', '$location', '$route', 'flash', 
                               'EventPlannerService', 
                               function ($scope, $location, $route, 
                                         flash, EventPlannerService) {

      $scope.msg = '';
      $scope.fEvent = {};

      EventPlannerService.VRegisterEvent().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }

        if ($scope.logout) {
            $location.path('/');
        }
      });

      $scope.VListEvents1 = function() {
        $location.path('/events');
      };

      $scope.fEventSubmitted = false;
      $scope.ACreateEvent0 = function(isValid) {
        $scope.fEventSubmitted = true;
        if (isValid) {
          EventPlannerService.ACreateEvent($scope.fEvent).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              if (label == '/events/new') {
                  $route.reload();
              } else {
                  $location.path(label);
              }
          });
        }
      };
}]);

EventPlannerModule.controller('ListEventsController', 
        ['$scope', '$location', '$route', 'flash', 'EventPlannerService',
    function ($scope, $location, $route, flash, EventPlannerService) {
      $scope.msg = '';
      EventPlannerService.VListEvents().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });

      $scope.VRegisterEvent0 = function() {
        $location.path('/events/new');
      };

      $scope.VHome1 = function() {
        $location.path('/VHome');
      };

      $scope.VShowEvent2 = function(eventId) {
        $location.path('/VShowEvent/'+eventId);
      };

      $scope.ADeleteEvent3 = function() {
        EventPlannerService.ADeleteEvent().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VListEvents') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};
}]);

