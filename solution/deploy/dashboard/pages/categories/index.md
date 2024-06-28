# Categories

```sql categories
    Select 
      Distinct category as name,
      'categories/' || category as link,
      count(category) as total
    from reviews
    group by 1
    having total > 1
```

{#each categories as category}

- [{category.name} ({category.total})](/categories/{category.name})

{/each}