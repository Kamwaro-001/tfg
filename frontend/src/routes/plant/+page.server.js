import { get_trees } from "$lib/features/trees.js";

/** @type {import('./$types').PageServerLoad} */
export async function load() {
  const response = await get_trees();
  return {
    response
  };
}