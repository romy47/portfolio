FROM nginx:1.19.0-alpine

# Copy the script to the image
COPY conditional_copy.sh conditional_copy.sh
RUN chmod +x conditional_copy.sh

# Run the script to copy the appropriate file
RUN conditional_copy.sh
