<script>
    /** @type {import('./$types').PageData} */
    export let data;
</script>

<svelte:head>
    <title>{data.community.name}</title>
</svelte:head>

<div class="community">
    <h2>{data.community.name}</h2>
    <p>{data.community.created_by}</p>
    <p>{data.community.visibility}</p>
    <p>{data.community.description}</p>
    <p>{data.community.date_created}</p>
</div>

