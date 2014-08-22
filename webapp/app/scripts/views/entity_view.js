app.Views.Entity = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/entity.html'],
  className: 'debt-entity',

  templateHelpers: function() {
    'use strict';

    var isACounty = this.model.get('issuerType') === 'county',
        isISD = this.model.get('issuerType') === 'isd',
        isACity = this.model.get('issuerType') === 'city',
        formatMoney = function(x) {
          return '$' + x.toFixed(0).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
        },
        formatPercent = function(u) {
          return u.toFixed(2).toString() + '%';
        };

    return {
      'isACounty': isACounty,
      'isISD': isISD,
      'isACity': isACity,
      'formatMoney': formatMoney,
      'formatPercent': formatPercent
    };
  },

  onRender: function() {
    'use strict';

    this.$el.addClass(this.model.get('issuerType'));
  }
});
