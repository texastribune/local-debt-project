app.Controllers.Main = Marionette.Controller.extend({
  index: function() {
    'use strict';
    this.searchController = new app.Controllers.Search();
    this.listenTo(this.searchController, 'location:found', this.locationFound);
  },

  locationFound: function(data) {
    'use strict';
    var self = this,
        issuer;

    this.entities = new app.Collections.Entities();
    _.each(data.issuers, function(dataIssuer) {
      issuer = new app.Models.Entity(dataIssuer.current);
      issuer.set('context', dataIssuer.context);
      self.entities.push(issuer);
    });

    this.renderButtons();

    this.entities.each(function(issuer) {
      if (issuer.get('issuerType') === 'county') {
        self.renderCounty(issuer);
      } else if (issuer.get('issuerType') === 'city') {
        self.renderCity(issuer);
      } else if (issuer.get('issuerType') === 'isd') {
        self.renderISD(issuer);
      }
    });
  },

  renderCounty: function(county) {
    'use strict';

    this.countyLayout = new app.Layouts.EntityLayout();
    app.countyRegion.show(this.countyLayout);
    this.countyLayout.debtBox.show(new app.Views.Entity({
      model: county
    }));
    this.countyLayout.debtByPop.show(new app.Views.PopulationContext({
      collection: new app.Collections.Entities(county.get('context').population)
    }));
    this.countyLayout.debtByAV.show(new app.Views.AVContext({
      collection: new app.Collections.Entities(county.get('context').assessedValuation)
    }));
  },

  renderCity: function(city) {
    'use strict';

    this.cityLayout = new app.Layouts.EntityLayout();
    app.cityRegion.show(this.cityLayout);
    this.cityLayout.debtBox.show(new app.Views.Entity({
      model: city
    }));
    this.cityLayout.debtByPop.show(new app.Views.PopulationContext({
      collection: new app.Collections.Entities(city.get('context').population)
    }));
    this.cityLayout.debtByAV.show(new app.Views.AVContext({
      collection: new app.Collections.Entities(city.get('context').assessedValuation)
    }));
  },

  renderISD: function(isd) {
    'use strict';

    this.isdRegion = new app.Layouts.EntityLayout();
    app.isdRegion.show(this.isdRegion);
    this.isdRegion.debtBox.show(new app.Views.Entity({
      model: isd
    }));
    this.isdRegion.debtByPop.show(new app.Views.StudentsContext({
      collection: new app.Collections.Entities(isd.get('context').students)
    }));
    this.isdRegion.debtByAV.show(new app.Views.ISDAVContext({
      collection: new app.Collections.Entities(isd.get('context').debtToAssessedValuation)
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
