# Reviews By Sentiment

```sql reviews
    select
        reviews_date
        category,
        sentiment,
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

 <DataTable
    data={reviews}
    search=true
/>



