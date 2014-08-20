app.Controllers.Search = Marionette.Controller.extend({
  initialize: function() {
    'use strict';

    this.baseURL = app.Settings.baseURL;
    this.searchView = new app.Views.Search();
    app.mainRegion.show(this.searchView);

    this.listenTo(this.searchView, 'search:string', this.searchByString);
    this.listenTo(this.searchView, 'search:location', this.searchByLocation);
  },

  searchByString: function(searchStr) {
    'use strict';

    $.get(this.searchURL(searchStr), function(data) {
      this.trigger('location:found', data);
    }).fail(function() {
      this.trigger('location:error', 'We could not find you.');
    });
  },

  searchByLocation: function() {
    'use strict';

    var locationFound,
        noGeolocation;

    locationFound = function(position) {
      $.get(this.locationURL(position), function(data) {
        this.trigger('location:found', data);
      });
    };

    noGeolocation = function() {
      this.trigger('location:error', 'Geolocation is not working.');
    };

    if ('geolocation' in navigator) {
      navigator.geolocation.getCurrentPosition(locationFound, noGeolocation);
    }
  },

  locationURL: function(position) {
    'use strict';

    var queryString = [
      'lat=' + position.coords.latitude,
      'lng=' + position.coords.longitude
    ].join('&');
    return this.baseURL + '/api/location?' + queryString;
  },

  searchURL: function(searchStr) {
    'use strict';

    return this.baseURL + '/api/search?q=' + searchStr;
  }
});