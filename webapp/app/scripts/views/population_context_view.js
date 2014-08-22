app.Views.PopulationContext = Marionette.CompositeView.extend({
  template: JST['app/scripts/templates/population_context.html'],
  childView: app.Views.ContextRow,
  childViewContainer: 'tbody',
});
