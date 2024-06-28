# {params.category}

```sql reviews
select
    rating,
    summary,
from reviews
where category = '${params.category}'
And summary is not null
group by rating, summary
order by rating desc

```
## Reviews Summary by Rating

<Dropdown 
    data={reviews} 
    name=category_selected
    value=rating 
    title="Select a Rating to See Summary"
/>

   
```sql summary
    select
        summary
    from reviews
    where category = '${params.category}' AND rating = '${inputs.category_selected.value}'
    and summary is not null
    group by summary
```

    
The summary of the reviews in category {params.category} with rating {inputs.category_selected.value} is: 

**{summary[0].summary}**


## Reviews along the Time

```sql reviews_by_date
    select
      reviews_date,
      count(*) as reviews
    from reviews
    where reviews_date is not null
    and category = '${params.category}'
    and rating = '${inputs.category_selected.value}'
    group by reviews_date, category, rating
    order by reviews_date DESC
````

<CalendarHeatmap 
    data={reviews_by_date}
    date=reviews_date
    value=reviews
    subtitle="Reviews by Date"
    filter=true
/>

## All Summary Reviews
<DataTable
    data={reviews}
    search=true
/>