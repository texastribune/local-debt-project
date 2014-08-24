app.Mixins.Helpers = {
  templateHelpers: function() {
    'use strict';

    var isACounty = this.model.get('issuerType') === 'county',
        isISD = this.model.get('issuerType') === 'isd',
        isACity = this.model.get('issuerType') === 'city',
        formatMoney = function(x) {
          if (typeof x === 'string' || x === null) {
            return 'N/A';
          } else {
            return '$' + x.toFixed(0).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
          }
        },
        formatPercent = function(x) {
          if (typeof x === 'string' || x === null) {
            return 'N/A';
          } else {
            return x.toFixed(4).toString() + '%';
          }
        },
        addCommas = function(x) {
          if (typeof x === 'string' || x === null) {
            return 'N/A';
          } else {
            return x.toFixed(0).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
          }
        };

    return {
      'isACounty': isACounty,
      'isISD': isISD,
      'isACity': isACity,
      'formatMoney': formatMoney,
      'formatPercent': formatPercent,
      'addCommas': addCommas
    };
  }
};
