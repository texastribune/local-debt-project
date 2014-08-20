app.Controllers.Main = Marionette.Controller.extend({
  index: function() {
    'use strict';
    this.searchController = new app.Controllers.Search();
    this.listenTo(this.searchController, 'location:found', this.locationFound);
  },

  locationFound: function(data) {
    'use strict';

    var county = new app.Models.Entity(data.current.county),
        city = new app.Models.Entity(data.current.city),
        ids = new app.Models.Entity(data.current.ids);

    this.entities = new app.Collections.Entities();
    this.entities.push(county);
    this.entities.push(city);
    this.entities.push(ids);

    this.entitiesView = new app.Views.Entities({
      collection: this.entities
    });

    app.cardsRegion.show(this.entitiesView);
  }
});
