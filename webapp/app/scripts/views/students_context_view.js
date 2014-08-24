app.Views.StudentsContext = Marionette.CompositeView.extend({
  template: JST['app/scripts/templates/students_context.html'],
  childView: app.Views.StudentsContextRow,
  childViewContainer: 'tbody',
});
