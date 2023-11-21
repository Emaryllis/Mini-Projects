const sqlite = require('better-sqlite3'), express = require('express'), app = express(), path = require('path'),
    { renderMains, renderDesserts, renderDrinks, renderPanel } = require('./render');
app.use(express.static(`${__dirname}/static`));
app.set('views', path.join(__dirname, '/static/ejs'));
app.use(express.urlencoded({ extended: true }));
app.set('view engine', 'ejs');
app.use(require('cookie-parser')());

const { mains, desserts, drinks } = JSON.parse(require('fs').readFileSync('items.json', 'utf8', (err, data) => { return err ? console.error(err) : data; }));
const [mainsMenu, dessertsMenu, drinksMenu, panel] = [renderMains(mains), renderDesserts(desserts), renderDrinks(drinks), renderPanel()];

app.get('/welcome', (req, res) => { res.clearCookie(...Object.keys(req.cookies)).render('welcome'); });
app.post('/welcome', (req, res) => { res.cookie('type', req.body.type).redirect('/menu'); });
app.get('/menu', (req, res) => { req.body.completed ? res.redirect('/welcome') : res.render('menu', { mainsMenu, dessertsMenu, drinksMenu, panel }); });
app.get('/payment', (req, res) => { res.render('payment'); });
app.get('/test', (req, res) => {
    res.render('numberIncrement');
})
app.use((req, res) => { res.status(404).redirect('/welcome'); });
app.listen(80, () => { console.info(`Server started on http://127.0.0.1`); });