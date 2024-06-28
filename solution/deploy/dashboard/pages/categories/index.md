# Categories

```sql categories
    Select 
      Distinct(primaryCategories) as name,
      'categories/' || primaryCategories as link,
      count(primaryCategories) as total
    from project.reviews
    group by 1
    having total > 1
```

{#each categories as category}

- [{category.name} ({category.total})](/categories/{category.name})

{/each}