export default function AboutSection() {
  const a = 1;
  return (
    <section className="py-20 mt-10">
      <div>New section</div>
      <div className="container mx-auto px-4 flex flex-col md:flex-row">
        <div className="md:w-1/2 mb-10 md:mb-0">
          <h2 className="text-3xl font-bold mb-4">About Datafund</h2>
          <p className="text-gray-600 mb-4">
            Datafund enables data owners to take control of their data,
            transform it into valuable, tradable assets, and connect with buyers
            who need quality data. Built on principles of privacy, control, and
            fairness, Datafund aims to reshape the data economy by empowering
            data owners and ethical data practices.
          </p>
          <div>New div</div>
          <div className="flex flex-col md:flex-row space-x-8 mx-2">
            <div>
              <h3 className="text-lg font-bold mb-2">
                Investors: We’ll start fundraising soon. Stay in the loop.
              </h3>
            </div>
          </div>
        </div>
        <div className="md:w-1/2 md:pl-10">
          <EmailSubscription className="mt-14" />
          {/* <textarea
              className="w-full p-2 border border-gray-300 rounded-md mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
              rows={4}
              placeholder="Message"
            ></textarea>
            <button
              type="submit"
              className="bg-black text-white px-6 py-2 rounded-md hover:bg-gray-800 transition duration-300"
            >
              Submit
            </button> */}
        </div>
      </div>
    </section>
  );
}
