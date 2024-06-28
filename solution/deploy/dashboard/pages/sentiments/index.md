# Reviews By Sentiment

```sql reviews
    select
        reviews_date
        category,
        sentiment,
        reviews_title,
        reviews_text
    from reviews
    where sentiment is not null
    order by category asc, rating desc
```
```sql pie_data
  select 
    sentiment as name, 
    count(*) as value
  from reviews
  where sentiment is not null
  group by sentiment
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

## All Reviews with Sentiment

<DataTable
    data={reviews}
    search=true
/>

```sql heatmap_data
    select
        rating,
        sentiment,
        count(*) as reviews
    from reviews
    WHERE sentiment is not null
    group by rating, sentiment
    order by rating DESC
```

## User Sentiment X Rating
 <Heatmap 
    data={heatmap_data} 
    x=rating 
    y=sentiment 
    value=reviews 
    colorPalette={['white', 'green']}
    title="Heatmap"
    subtitle="Sentiment by Rating"
    filter=true
    link=link
/>

