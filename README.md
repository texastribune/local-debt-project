# Debt Project

## Databases

``` python
{
  'FY 2013 Texas City Debt Outstanding': '13CITYTRLP.xls',
  'FY 2013 Texas County Debt Outstanding': '13CNYTRLP.xls',
  'FY 2013 Texas Independent School District (ISD)Debt Outstanding':'13ISDvaMOrvLP.xls'
}
```

## City and County databases

We're only interested in the first sheet: "Tax-Supported Debt"
For each city/county, we want the users to see the info in columns F, G, H, K and N.
F - Debt Outstanding
G - Interest Owed on that debt
H - Total Debt Service (F+G)
K - Population
N - Debt Outstanding Per Capita

## School district debt
We're interested in TWO sheets: "13VotedDebt" and "13M&O Debt." (There are about 1,000 ISDs. Most have Voted Debt. About 180 also have M&O Debt, so for most ISDs, the M&O line will read "0")
For each sheet, we're interested in F, G and H (same as with City and County Debt) and N. which is "Full Year ADA2012" (student enrollment).
We want to show "Debt Outstanding Per Student" but the state data doesn't do the math for us in the way I want so we'll need to plug it in ourselves. For each district, we want the following: (Voted Debt Outstanding + M&O Debt Outstanding)/ADA2012.


## Note

Finally, I want us to do something similar to the "How MY CITY Compares" box that the Comptroller uses on her Local Debt website. I'm fine copying their approach or doing something different. Just want the user to have a way to see how their city/county/ISD compares to others.


## Links

* http://www.brb.state.tx.us/lgs/lgspubs2013.aspx
* http://www.brb.state.tx.us/pub/lgs/fy2013/13CITYTRLP.xls
* http://www.brb.state.tx.us/pub/lgs/fy2013/13CNYTRLP.xls
* http://www.brb.state.tx.us/pub/lgs/fy2013/13ISDvaMOrvLP.xls

http://www.texastransparency.org/Special_Features/Debt_at_a_Glance/counties.php

## Setup

You are going to need PostgreSQL. If your are using OSX, we recommend [Postgres.app](http://postgresapp.com/). You will need to have a database called `local_debt`:

```sql
CREATE DATABASE local_debt;
```

Then you need to run:

    pip install -r requirements.txt
    make resetdb

You will also need to setup the **webapp**. Just run:

    cd webapp
    npm install -g grunt-cli bower
    npm install && bower install
    grunt serve

  Feel free to start hacking.
