<div class="plant-form">
  <form method="post">
    <label for="genus">Genus</label>
    <input type="text" id="genus" name="genus" />
    <label for="more_info">More info</label>
    <input type="text" id="more_info" name="more_info" />
    <label for="files">Upload a file</label>
    <input type="file" id="files" name="files" />
    <button type="submit">Add</button>
  </form>
</div>

<style>
    .plant-form {
        display: flex;
        flex-direction: column;
        margin-left: auto;
        margin-right: auto;
    }
    form {
        display: flex;
        flex-direction: column;
        margin-left: auto;
        margin-right: auto;
    }
    label {
        margin-top: 1em;
    }
    input {
        margin-top: 0.5em;
    }
    button {
        margin-top: 1em;
    }
</style>
