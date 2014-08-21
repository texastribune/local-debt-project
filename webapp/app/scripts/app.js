window.app = new Marionette.Application();

app.Collections = app.Collections || {};
app.Controllers = app.Controllers || {};
app.Layouts = app.Layouts || {};
app.Models = app.Models || {};
app.Routers = app.Routers || {};
app.Views = app.Views || {};

app.Settings = {
  'baseURL': 'http://localhost:8000'
};

app.addRegions({
  'searchRegion': '#search',
  'goToRegion' : '#go-to-buttons',
  'countyRegion': '#county-region',
  'cityRegion': '#city-region',
  'isdRegion': '#isd-region'
});

app.Routers.Main = Backbone.Marionette.AppRouter.extend({
  appRoutes: {
    '': 'index'
  }
});

app.addInitializer(function() {
  'use strict';

  this.mainRouter = new app.Routers.Main( {
    controller: new app.Controllers.Main()
  });

  if ( Backbone.history ) {
    Backbone.history.start();
  }
});

$(document).ready(function(){
  'use strict';

  app.start();
});
