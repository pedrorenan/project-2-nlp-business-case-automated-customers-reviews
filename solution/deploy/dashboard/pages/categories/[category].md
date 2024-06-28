# {params.category}

```sql reviews
select
    count(*) as total 
from project.reviews
where primaryCategories = '${params.category}'
```


{params.category} received <Value data={reviews} column=total /> reviews.