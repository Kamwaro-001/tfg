import { add_tree } from "$lib/features/trees.js";

export const actions = {
  default: async ( { request }) => {
    const form = await request.formData();

    /** @type {object} */
    const plant = {
      genus: form.get('genus'),
      more_info: form.get('more_info'),
      files: form.get('files')
    }

    /** @type {object} */
    const response = await add_tree(plant);
    console.log(response)
  }
}