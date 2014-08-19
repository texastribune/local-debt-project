window.app = new Marionette.Application();

app.Views = app.Views || {};
app.Controllers = app.Controllers || {};
app.Routers = app.Routers || {};

app.addRegions({
  'mainRegion': '#main'
});

app.Routers.Main = Backbone.Marionette.AppRouter.extend({
  appRoutes: {
    '': 'index'
  }
});

app.addInitializer(function() {
  'use strict';

  this.mainRouter = new app.Routers.Main( {
    controller: new app.Controllers.MainController()
  });

  if ( Backbone.history ) {
    Backbone.history.start();
  }
});

$(document).ready(function(){
  'use strict';

  app.start();
});
