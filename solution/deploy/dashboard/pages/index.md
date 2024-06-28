
# Ironhack Project 2

<LastRefreshed prefix="This dashboard was updated"/>

<Details title="Disclaimer">
    
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

</Details>


```sql categories
    Select 
      Distinct(category) as name,
      'categories/' || category as link,
      count(category) as total,
      rating
    from reviews
    group by category, rating
    having total > 2
    order by category ASC, rating DESC
```



## Reviews by Category and Rating

<DataTable
    data={categories}
    link=link
    search=true
>
    <Column id=name label=Category />
    <Column id=rating contentType=colorscale scaleColor=green/>
    <Column id=total label=Total />
</DataTable>

 <Heatmap 
    data={categories} 
    x=rating 
    y=name 
    value=total 
    colorPalette={['white', 'green']}
    title="Heatmap"
    subtitle="By Category and Rating"
    filter=true
    link=link
/>

```sql pie_data
  select 
    category as name, 
    count(*) as value
  from reviews
  group by category
  having value > 2
```
## Reviews by Category
<Grid cols=2>
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
</Grid>

```sql reviews_by_date
    select
      reviews_date,
      count(*) as reviews
    from reviews
    where reviews_date is not null
    group by reviews_date
    order by reviews_date DESC
````

## Reviews along the Time

<CalendarHeatmap 
    data={reviews_by_date}
    date=reviews_date
    value=reviews
    subtitle="Reviews by Date"
    filter=true
/>


 






