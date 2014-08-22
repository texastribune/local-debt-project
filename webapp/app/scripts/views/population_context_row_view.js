app.Views.PopulationContextRow = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/population_context_row.html'],
  tagName: 'tr'
});

_.extend(app.Views.PopulationContextRow.prototype, app.Mixins.Helpers);
