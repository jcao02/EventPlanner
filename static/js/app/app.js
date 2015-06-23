// Creación del módulo de la aplicación
var EventPlannerModule = angular.module('EventPlanner', 
                                        ['ngRoute', 'ngAnimate', 'flash']);

EventPlannerModule.run(["$rootScope", "$location", "$route", "flash", "EventPlannerService", 
                       function ($rootScope, $location, $route, flash, EventPlannerService) {
    $rootScope.LogOut = function() {
          EventPlannerService.ALogOutUser().then(function (object) {
            var msg = object.data["msg"];
            if (msg) flash(msg);
            $rootScope.res = object.data;
            for (var key in object.data) {
                $rootScope[key] = object.data[key];
            }

            var label = object.data["label"];
            if (label == "/VHome") {
                $route.reload(); 
            } else {
                $location.path(label); 
            }
          })
      };

    $rootScope.VHome = function() {
        $location.path('/VHome');
      };


}])
// Routing
EventPlannerModule.config(function ($routeProvider) {
    $routeProvider
    .when('/', { // Root
        controller: 'LoginUserController',
        templateUrl: 'app/EventPlanner/user/login.html'
    });
});

// General controller
EventPlannerModule.controller('EventPlannerController_',  ['$scope', '$http', '$location',
        function($scope) {
            $scope.title = "DiseñoAplicaciónEventos";
        }]);

EventPlannerModule.directive('file', function () {
    return {
        restrict: 'A',
    scope: {
        file: '='
    },
    link: function (scope, el, attrs) {
        el.bind('change', function (event) {
            var file = event.target.files[0];
            scope.file = file ? file : undefined;
            scope.$apply();
        });
    }
    };
});
