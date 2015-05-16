EventPlannerModule.service('EventPlannerService', ['$q', '$http', function($q, $http) {

    this.ACreateUser = function(fUser) {
        return  $http.post( 
                          "/eventplanner/ACreateUser",
                          { data: fUser}
                         );
    //    var labels = ["/VLoginUser", "/VRegisterUser", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VRegisterUser = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'eventplanner/VRegisterUser',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ALoginUser = function(fLogin) {
        return  $http({
          url: "eventplanner/ALoginUser",
          data: fLogin,
          method: 'POST',
        });
    //    var labels = ["/VHome", "/VLoginUser", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VLoginUser = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'eventplanner/VLoginUser',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AEvents = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'eventplanner/AEvents',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VListEvents", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VHome = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'eventplanner/VHome',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACreateEvent = function(fEvent) {
        return  $http({
          url: "EventPlanner/ACreateEvent",
          data: fEvent,
          method: 'POST',
          headers: { 'Content-Type': 'multipart/form-data' },
          transformRequest: function (data, headersGetter) {
                var formData = new FormData();
                angular.forEach(data, function (value, key) {
                    formData.append(key, value);
                });

                var headers = headersGetter();
                delete headers['Content-Type'];

                return formData;
          }    });
    //    var labels = ["/VShowEvent", "/VRegisterEvent", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VListEvents = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/VListEvents',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ADeleteEvent = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/ADeleteEvent',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VListEvents", "/VListEvents", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VShowEvent = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/VShowEvent',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ADeleteUser = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/ADeleteUser',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VListUsers", "/VListUsers", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.AEditEvent = function(fEvent) {
        return  $http({
          url: "EventPlanner/AEditEvent",
          data: fEvent,
          method: 'POST',
          headers: { 'Content-Type': 'multipart/form-data' },
          transformRequest: function (data, headersGetter) {
                var formData = new FormData();
                angular.forEach(data, function (value, key) {
                    formData.append(key, value);
                });

                var headers = headersGetter();
                delete headers['Content-Type'];

                return formData;
          }    });
    //    var labels = ["/VShowEvent", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VEditEvent = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/VEditEvent',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AReserveEvent = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/AReserveEvent',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VShowEvent", "/VShowEvent", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VRegisterEvent = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/VRegisterEvent',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AUsers = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'eventplanner/AUsers',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VListUsers", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VListUsers = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'eventplanner/VListUsers',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AGenerateCredentials = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/AGenerateCredentials',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VCredential", "/VShowEvent", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VCredential = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/VCredential',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AGenerateCertificate = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/AGenerateCertificate',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VCertificate", "/VShowEvent", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VCertificate = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/VCertificate',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACancelReservation = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/ACancelReservation',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VShowEvent", "/VShowEvent", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.ALogOutUser = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/ALogOutUser',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VLoginUser", "/VHome", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.AVerifyAssitance = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'EventPlanner/AVerifyAssitance',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VListUsers", "/VListUsers", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
}]);
