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
        isd = new app.Models.Entity(data.current.isd);

    this.entities = new app.Collections.Entities();
    this.entities.push(county);
    this.entities.push(city);
    this.entities.push(isd);

    this.renderButtons();
    this.renderCounty(county, data);
    this.renderCity(city, data);
    this.renderISD(isd, data);
  },

  renderCounty: function(county, data) {
    'use strict';
    this.countyLayout = new app.Layouts.EntityLayout();
    app.countyRegion.show(this.countyLayout);
    this.countyLayout.debtBox.show(new app.Views.Entity({
      model: county
    }));
    this.countyLayout.debtByPop.show(new app.Views.PopulationContext({
      collection: new app.Collections.Entities(data.population.county)
    }));
    this.countyLayout.debtByAV.show(new app.Views.AVContext({
      collection: new app.Collections.Entities(data.debtToAssessedValuation.county)
    }));
  },

  renderCity: function(city, data) {
    'use strict';
    this.cityLayout = new app.Layouts.EntityLayout();
    app.cityRegion.show(this.cityLayout);
    this.cityLayout.debtBox.show(new app.Views.Entity({
      model: city
    }));
    this.cityLayout.debtByPop.show(new app.Views.PopulationContext({
      collection: new app.Collections.Entities(data.population.city)
    }));
    this.cityLayout.debtByAV.show(new app.Views.AVContext({
      collection: new app.Collections.Entities(data.debtToAssessedValuation.city)
    }));
  },

  renderISD: function(isd, data) {
    'use strict';
    this.isdRegion = new app.Layouts.EntityLayout();
    app.isdRegion.show(this.isdRegion);
    this.isdRegion.debtBox.show(new app.Views.Entity({
      model: isd
    }));
    this.isdRegion.debtByPop.show(new app.Views.StudentsContext({
      collection: new app.Collections.Entities(data.debtPerStudent.isd)
    }));
  },

  renderButtons: function() {
    'use strict';
    this.goToButtons = new app.Views.GoToButtons({
      collection: this.entities
    });

    app.goToRegion.show(this.goToButtons);
  }
});
