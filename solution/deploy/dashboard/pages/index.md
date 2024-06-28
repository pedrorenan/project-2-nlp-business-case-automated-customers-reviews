
# Ironhack Project 2

<LastRefreshed prefix="Data last updated"/>

<Alert>
This is a student project
</Alert>

<Alert status="info">
This data is from Amazon Reviews Dataset
</Alert>

<Alert status="success">
We have lerned a lot about NPL, LSTM and BERT
</Alert>

<Alert status="warning">
The data is not perfect, but we have done our best
</Alert>

<Alert status="danger">
Do not use this data for any real-world applications
</Alert>

<Details title="Disclaimer">
    
This is a student project. The data is from Amazon Reviews Dataset. We have learned a lot about NPL, LSTM and BERT. The data is not perfect, but we have done our best. Do not use this data for any real-world applications.

</Details>

<Tabs>
    <Tab label="First Tab">
        Content of the First Tab

        You can use **markdown** here too!
    </Tab>
    <Tab label="Second Tab">
        Content of the Second Tab

        Here's a [link](https://www.google.com)
    </Tab>
</Tabs>

<Modal title="Title" buttonText='Open Modal'> 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

<Heatmap 
    data={categories} 
    x=rating 
    y=name 
    value=total 
    colorPalette={['white', 'green']}
    title="Reviews"
    subtitle="By Category and Rating"
    filter=true
/>

</Modal>

```sql categories
    Select 
      Distinct(primaryCategories) as name,
      'categories/' || primaryCategories as link,
      count(primaryCategories) as total,
      rating
    from project.reviews
    group by primaryCategories, rating
    having total > 2
    order by primaryCategories ASC, rating DESC
```

<Dropdown 
    data={categories} 
    name=category 
    value=name 
    title="Select a Category" 
/>

### Button
<LinkButton url='/categories/Acecssories'>
  Accessories
</LinkButton>

<DataTable
    data={categories}
    link=link
    search=true
>
    <Column id=name label=Category />
    <Column id=rating contentType=colorscale scaleColor=green/>
</DataTable>

```sql reviews_by_date
    select
      date,
      count(*) as reviews
    from project.reviews
    group by date
    order by date
````

<CalendarHeatmap 
    data={reviews_by_date}
    date=date
    value=reviews
    title="Calendar Heatmap"
    subtitle="Reviews by Date"
    filter=true
/>

```sql reviews_dimensions
    select
     *
    from project.reviews
```

### Dimension Grid
<DimensionGrid data={reviews_dimensions} />


<Grid cols=2>
    <LineChart data={reviews_by_date} x=date y=reviews/>
    <BarChart data={reviews_by_date} x=date y=reviews fillColor=#00b4e0/>
    <ScatterPlot data={reviews_by_date} x=date y=reviews fillColor=#015c08/>
    <AreaChart data={reviews_by_date} x=date y=reviews fillColor=#b8645e lineColor=#b8645e/>
</Grid>

<LineChart data={reviews_by_date} x=date y=reviews/>
  <BarChart data={reviews_by_date} x=date y=reviews fillColor=#00b4e0/>
  <ScatterPlot data={reviews_by_date} x=date y=reviews fillColor=#015c08/>
  <AreaChart data={reviews_by_date} x=date y=reviews fillColor=#b8645e lineColor=#b8645e/>

  <Heatmap 
    data={categories} 
    x=rating 
    y=name 
    value=total 
    colorPalette={['white', 'green']}
    title="Reviews"
    subtitle="By Category and Rating"
    filter=true
/>

<Histogram
    data={reviews_by_date} 
    x=reviews 
/>

<BigValue 
  data={categories} 
  value=total
  comparison=rating
  comparisonTitle="Last Month"
  comparisonDelta=false
/>

```sql pie_data
  select 
    primaryCategories as name, 
    count(*) as value
  from project.reviews
  group by primaryCategories
  having value > 2
```

<ECharts config={
    {
        tooltip: {
            formatter: '{b}: {c} ({d}%)'
        },
        series: [
        {
          type: 'pie',
          data: [...pie_data],
        }
      ]
      }
    }
/>

<ECharts config={
    {
        tooltip: {
            formatter: '{b}: {c} ({d}%)'
        },
      series: [
        {
          type: 'pie',
          radius: ['40%', '70%'],
          data: [...pie_data],
        }
      ]
      }
    }
/>

<ECharts config={
    {
      title: {
        text: 'Treemap Example',
        left: 'center'
      },
        tooltip: {
            formatter: '{b}: {c}'
        },
      series: [
        {
          type: 'treemap',
          visibleMin: 300,
          label: {
            show: true,
            formatter: '{b}'
          },
          itemStyle: {
            borderColor: '#fff'
          },
          roam: false,
          nodeClick: false,
          data: [...pie_data],
          breadcrumb: {
            show: false
          }
        }
      ]
      }
    }
/>

Sofia and Faisal, see all possible chart types [here](https://echarts.apache.org/examples/en/index.html)

